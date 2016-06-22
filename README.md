# pythontumblrbot

A bot for Tumblr, written in Python, that forms a Markov chain out of all the previous questions asked and answers each new question with 2-4 sentences formed from that Markov chain. Uses a modified version of Rob Dawson's [markov-text](https://github.com/codebox/markov-text) for Markov-chain bits.

## Dependencies:

- pytumblr, with changes made to add 'answer' and 'state' valid arguments
