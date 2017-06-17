#!/usr/bin/python

# Author: Utku Tarhan

# Requires twython package which could be installed: sudo pip install twython

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import os
import time
import random
from twython import Twython
# your twitter access information goes here

apiKey = 'REPLACEME'
apiSecret = 'REPLACEME'
accessToken = 'REPLACEME'
accessTokenSecret = 'REPLACEME'

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def randomTweet():
    try:
        tweetsloc = open(os.path.join(__location__,'tweets.txt'),'r')
        tweetsList = tweetsloc.readlines()
        tweetsloc.close()
        randomise = random.randrange(len(tweetsList))
        print (tweetsList[randomise]) #For debugging
	api.update_status(status=tweetsList[randomise])
        return None
    except IOError:
        return None
	
randomTweet()
