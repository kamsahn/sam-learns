# Wikimedia server

Use this server to retrieve article view counts and related information from wikimedia

## Use

To use this tool:

- Clone this repo to your local file system `git clone []` where `[]` is the copied value from GitHub using whichever format you choose.

- Install dependencies locally by running `npm install` in the root directory of the project.
    
- Start the server by running `npm start` in the root directory of the project.

- Use the following guide to run curl commands in a **separate terminal window**:

### Retrieve the day of the month where an article got the most page views

data attributes:
- article (required): Name of wiki article per wikimedia.
- startDateString (required): Date string with format YYYYMMDD. Must be a date further than 1 day in the past due to wikimedia limitations.

Copy the following code block into a separate terminal from the server and execute. Change the attributes while testing the application:
```
curl -H "Content-Type: application/json" \
-d '{"article":"YouTube","startDateString":"20230701"}' \
http://localhost:3000/highDay
```

### Retrieve a list of the most viewed articles for ~~a week or~~ a month (if an article is not listed on a given day, you can assume it has 0 views)

data attributes:
- year (required): Year in YYYY format.
- month (required): Month in MM.
- day (optional): Day in DD format OR "all-days" to receive data for all days of the month. Defaults to "all-days". Must be a date further than 1 day in the past due to wikimedia limitations.
- limit (optional): Limit of articles retrieved as a string integer. Defaults to 10.

Copy the following code block into a separate terminal from the server and execute. Change the attributes while testing the application:
```
curl -H "Content-Type: application/json" \
-d '{"year":"2024","month":"01","day":"all-days","limit":"5"}' \
http://localhost:3000/mostViewed
```

### Retrieve the view count of a specific article for a week or a month

data attributes:
- article (required): Name of wiki article per wikimedia.
- startDateString (required): Date string with format YYYYMMDD. Must be a date further than 1 day in the past due to wikimedia limitations.
- duration (optional): "weekly" to get 7 days past the start date or "monthly" do get all days of start day month. Defaults to 0.

Copy the following code block into a separate terminal from the server and execute. Change the attributes while testing the application:
```
curl -H "Content-Type: application/json" \
-d '{"article":"Berlin","startDateString":"20230701","duration":"monthly"}' \
http://localhost:3000/viewCount
```

## Test

In the root directory, run
```
npm test
```
to execute all available tests.

## Author's Notes

Overall, this is a wrapper for the existing wikipedia provided API pageview.js.
When looking over the wikimedia link provided, I found that to be nicely documented and formated to my use.
Would I ever use this API over the existing pageview.js API? No. I imagine they spent more than 5 hours developing that and certainly has much better test coverage than my project.

Speaking of testing, I noteably left out some major tests like testing the meat of the router and any e2e server tests. This decision was made in favor of delivering within the time box and not an ommission because I didn't think it was important (it's very important).
The system also expects the user to format the requests properly and doesn't do any checks on it's own. The server will just error out if some key attributes are left out or malformed.

Also noteably left out is the functionality to retrieve a list of most viewed articles on a weekly timeframe (vs. only a monthly timeframe). The way `pageviews.js` is set up, I only found a way to do this with 7 calls of the daily `getTopPageviews` endpoint. I'm sure there is a way to configure this properly to only make one call, but I skipped this in favor of time.

Looking back at the whole project, a tool like `swagger` would have been very useful in spinning up easy to read docs and endpoints, but I figured this project lightweight enough to skip. In a real world application, I would look to use that.

I tried my best to maintain within the 5 hour timeline (despite my many google searches for silly gotchas like "import vs require node js" or "how to import a function from file jest node js"). This resulted in some design cuts (as I mentioned) as well as lack of test coverage (also mentioned). I've also written this readme outside that window.
I will also be transparent about some of the logic in this, lots of little functions like the reduce function to get the date object with the highest view count or the `addDays` function in the `Date.prototype` were taken from google searches. No need to reinvent the wheel, especially on the timeline given. But that's also how I would develop in real life.

In summary, here is a list of future improvements:
- Improve testing coverage (e2e as declared above or malformed data checks).
- Complete weekly requirement of mostViewed articles.
- Make *any sort of* UI improvements (even just a basic html form).
- Use something more sophisticated than a switch operator as a router.

All in all, it was good to take a look back at some of the basics. So much of my recent work has taken all this set up for granted (as I assume most developers can say who aren't working on "0 to 1" codebases).
I hope you enjoy (?) looking through this project and I look forward to hearing your feedback.
