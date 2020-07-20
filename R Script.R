#Import Libaries
library(readr)
library(dplyr)
library(jsonlite)

### INITIAL PROCESSING

#Read provided IMDB files
Title <- read_delim("../Title.tsv", "\t", escape_double = FALSE, trim_ws = TRUE)
Episode <- read_delim("../Episode.tsv", "\t", escape_double = FALSE, trim_ws = TRUE)
Ratings <- read_delim("../Ratings.tsv", "\t", escape_double = FALSE, trim_ws = TRUE)
Names <- read_delim("../Names.tsv", "\t", escape_double = FALSE, trim_ws = TRUE)

#Some Basic merging of Title, Episodes, and Rating
colnames(Title)[1] <- 'parentTconst'
Episodes <- merge(x = Episode, y = Title, by = 'parentTconst', all.x = TRUE)
Ratings <- merge(x = Ratings, y = Episodes, by = 'tconst', all.x = T)

#Changing type of variables to numeric
Ratings[,5] <- as.integer(Ratings[,5])
Ratings[,6] <- as.integer(Ratings[,6])

#Remove movies and stuff, remove less commonly seen shows and then arrange
Shows <- Ratings %>% filter (seasonNumber != '<NA>') %>% filter(primaryTitle != '<NA>') %>% arrange(originalTitle, seasonNumber, episodeNumber) 
Compressed_Shows <- Shows %>% group_by(parentTconst) %>% summarize(averageVotes = mean(numVotes))
Shows <- merge(Shows, Compressed_Shows, by = 'parentTconst', all.x = TRUE)
nrow(Shows %>% filter(averageVotes >= 163))
Shows <- Shows %>% filter(averageVotes >= 163) %>% arrange(originalTitle, seasonNumber, episodeNumber) 

#Separating by columns and binding together what we need.
Name <- Shows[,8]
Season <- as.integer(Shows[,5])
Rating <- as.numeric(Shows$averageRating)
Episode <- as.integer(Shows[,6])
Code <- Shows[,2]
Link <- paste( (rep('https://www.imdb.com/title/', length(Shows[,2]))) , Code, '/', sep = '')

#This is our final dataframe before scraping. 
Final <-data.frame(Code, Name, Season, Episode, Rating, Link)
cols <- c( 'Season' , 'Episode' )
Final$index <- apply( Final[ , cols ] , 1 , paste , collapse = "-" )

#Write the list of codes and links for us to scrape now
write.csv(Code, 'Code.csv')
write.csv(Link, 'Link.csv')




### AFTER WE HAVE SCRAPED THE MAIN INFO WITH SCRAPY


#Merge together our final dataset with the scraped info
Scraped_Info <- read.csv("../Main_Info.csv", encoding = "UTF-8", na.strings = 'NA')
df <- merge(x = Final, y = Scraped_Info, by = "Code", all.x = TRUE) 

#Reading in Images and then merging it
Image_2 <- read.csv('../Images.csv')
head(Image_2)
df <- merge(x = df, y = Image_2, by = 'Code', all.x = TRUE)
df$Actual_Link[grep("http", df$Image)] <- as.character(df$Image)[grep("http", df$Image)]
#Make sure to delete Image
df <- df[, -14]

#Arrange it in order
df <- df %>%  arrange(Name, Season, Episode)

#Double check
head(df)
write.csv(df, 'Final.csv', fileEncoding = "UTF-8")
