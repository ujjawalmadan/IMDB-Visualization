# IMDb-Visualization
<h2><a href="https://imdb-d3visualization.herokuapp.com/index.html" target = '_blank'>IMDb Ratings Visualization - d3.js</a></h2>
                            <h6>Description</h6>
                            <p>This visualization allows one to view a show of their liking and visualize the episode ratings in chronological order. 
                                If one hovers over an episode, then the episode information as well as a screenshot from the episode will be shown.
                                If one clicks on the episode, they will be redirected to the IMDb page directly. I recommend you explore the live demo (link at the bottom of the page) and see the ratings of your favourite shows! 
                            </p>
                            <h6>Motivation</h6>
                            <p>
                                The true motivation for this project came actually from watching The Simpsons. 
                                As some of you may know, Simpsons episodes can be sometimes hit or miss and I wanted to be able to go through the entire 20+ seasons without watching the low-rated episodes. 
                                This visualization allows me to do just that! I could even prioritize which epiodes to watch, going from highest-rated to lowest-rated.
                                Given that I knew in advance that Georgia Tech has a rigorous Data and Visual Analytics Course which requires students to learn d3.js, I decided to learn and implement a project in d3 whilst also accomplish my goal of visualizing show ratings.
                                As they say, two birds with one stone.
                            </p>       
                            <h6>Business Value</h6>
                            <p>The visualization itself can be utilized by avid TV viewers to monitor the ratings of their favourite shows, or even be used in a context like I described above. 
                                The scraped data itself has a lot of value and can be used in regression based prediction tasks or more complex NLP analyses (using plot and reviews information).
                                The data can also be aggregated with other sources (such as Rotten Tomatoes data) with which, one could perform even more complex tasks and derive more impactful insights.
                            </p>
                            <h6>Process</h6>
                            <ol>
                                <li>Web Scraping - Using Scrapy and Splash</li>
                                <li>Preprocessing - Using R</li>
                                <li>Visualization - Using HTML/CSS/JS and d3.js</li>
                                <li>Deployment - Using Heroku</li>
                            </ol> 
                            <h6>Challenges</h6>
                            <p>
                                One of the initial challenges was simply scraping the data while staying undetected. I used a proxy server, and set manual delays so that my access to IMDb would not be revoked. 
                                Either IMDb was quite lenient or my safeguards were enough to slip past them. The biggest challenge no doubt was learning and programming this visualization in d3.js. 
                                As those of whom that have used d3.js may be agree with, d3.js is not very intuitive and requires manually coding many of the functions that we take for granted in visualization packages such as Matplotlib and ggplot. 
                                There were many look ups on Stack Overflow, and many online tutorials. After several face-palms and long nights however, I managed to complete it.  
                            </p> 

