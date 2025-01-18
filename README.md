# Code Finder

## Making your code search experience better!  

### Check it out on [codefinder.dev](https://codefinder.dev/)
 
> Disclaimer: This website is not affiliated with GitHub and has no connection to its owner, stakeholder, contributors, or any others.  
> For the official GitHub Search website click [here](https://github.com/search)

<br>


[![Latest release](https://badgen.net/github/release/DanielDekhtyar/CodeFinder)](https://github.com/DanielDekhtyar/CodeFinder/releases)
![Python badge](https://img.shields.io/badge/python-3.12.8-blue)
![Monthly users badge](https://img.shields.io/badge/users-4.9K/month-blue)
[![GitHub commits](https://badgen.net/github/commits/DanielDekhtyar/CodeFinder)](https://GitHub.com/DanielDekhtyar/CodeFinder/commit/)
[![GitHub latest commit](https://badgen.net/github/last-commit/DanielDekhtyar/CodeFinder)](https://GitHub.com/DanielDekhtyar/CodeFinder/commit/)
[![Website status badge](https://img.shields.io/website-up-down-green-red/http/codefinder.dev)](https://codefinder.dev/)
[![Website badge](https://img.shields.io/badge/URL-codefinder.dev-blue)](https://codefinder.dev/)


<br>

## About this project
---

## Introduction
The idea of this project arose from a personal frustration: the lack of an efficient way to easily find small scripts for my various personal projects. Despite searching extensively, no satisfactory solution was found. Faced with this problem, My initial idea was to create a website where people could present their scripts, and give a link to the respective GitHub repositories, so those looking for a script could find whatever they were looking for and then go to GitHub to get the code for the script they needed.

## The Problem
After giving a second thought to the idea of a dedicated website for script sharing I understood that there was no need to reinvent the wheel and I could just use GitHub to search for the repositories that I needed. That's it! Problem solved! Or is it? It turned out that GitHub's native search engine, while powerful, demanded users to navigate complex syntax and special keywords, akin to deciphering code in a challenging programming language, just to get the results they were looking for. This realization prompted a rethink of the approach, recognizing the potential for a more streamlined solution.

## Solution
As we are going full steam ahead into the AI age, it would be foolish not to utilize its magical power to help me solve this problem. By fine-tuning OpenAI's GPT-3.5-Turbo LLM model, I taught it to receive user requests in plain English, interpret and translate them into precise GitHub search queries utilizing all the tricks and keywords to get the best results that the user is looking for! This novel approach eliminates the need for users to grapple with arcane syntax, offering a seamless and intuitive search process. The fusion of human-like language understanding with robust AI capabilities marks a significant leap forward in simplifying code discovery.

## Technical Details
At the heart of the system lies a sophisticated algorithmic pipeline. User requests are transmitted to the fine-tuned AI model via OpenAI's API, where they undergo intricate language processing. Upon receiving the model's response, the system dynamically formulates optimized GitHub search queries tailored to the user's intent. Leveraging GitHub's Search API, the system retrieves a comprehensive JSON dataset of relevant repositories. These results are then meticulously presented through a user-friendly interface, ensuring accessibility and clarity.

## Future Plans
I have many plans to make this website as good as passable to give developers an easy way to search through GitHub. My future efforts will focus on enhancing the AI model's capabilities, refining its ability to generate precise queries and delivering even more relevant search results. Additionally, addressing the shortcomings of GitHub's default ranking algorithm is a priority. Plans include developing a bespoke ranking system to prioritize results based on user preferences and relevance, ensuring an unparalleled search experience.

## The main page of the website is just a search bar :
![Code Finder main page](<Code Finder main page.png>)

<br>

## Here is an example of a result page:
We are trying to look for ***machine learning data analytics and visualization script with Matplotlib***.  
Here is what the results might look like:

![Code Finder results page](<Code Finder results page.png>)


### You can try it yourself on [codefinder.dev](https://codefinder.dev/)
