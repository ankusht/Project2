# Scrapex
Webapp url : https://frozen-waters-22551.herokuapp.com/

Resources Used
==
- ## Microsoft Text Analytics :
> + Although sentiment analysis was a major part in development of our app, and 6 days was not sufficient to wrote our own code for that which may give us good accuracy.
> + So we thought of using [Text Analytics API][text_api] which is one of the best available sources for sentiment analysis and own a user friendly documentation
> + In our project the file ` myapp/lib/sentiment.py` contains the `module` to call the Text Analysis API

- ## Facebook Graph API :
> + We needed to extract comments from facebook comments, so we used [Facebook Graph API][graph api] to achieve that.
> + In our project, `module` contained by `myapp/lib/fb_comments.py` does that task for us.

- ## Youtube Comment APU : 
> + Similar to facebook, we tried to expand our idea to youtube also .
> + To extract comments from youtube we used [Youtube Comment API][comment api].
> + `module` contained by `myapp/lib/yt_comments.py` extracts the comments from any youtube video.
> + **Note :** Although `Youtube Comment API` is sufficient enough to extract the comments form youtube videos, but it uses `Oauth2` authentication to authenticate users and that uses terminal console. So till now it works in localhost only but we are trying to figure out an alternative for it.

Deploying Locally
==
<!-- Add the doc. here -->
## Possible Errors
#### Wrong Url :
> May return an error in case of wrong url

#### NO comments
> May return an error if there are no comments on your video,so use video with comments only.

#### Analysis on Youtube
> Due to some Oauth2 errors with youtube API, right now our app supports youtube analysis on localhost only.
> Deployed version doesn't support youtube analysis


[text_api]: https://azure.microsoft.com/en-in/services/cognitive-services/text-analytics/
[graph api]: https://developers.facebook.com/docs/graph-api/
[comment api]: https://developers.google.com/youtube/v3/docs/commentThreads
