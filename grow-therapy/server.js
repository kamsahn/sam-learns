const http = require('http');
const pageviews = require('pageviews');
const qs = require('querystring');

const hostname = '127.0.0.1';
const port = 3000;

// Helper methods
Date.prototype.addDays = function(days) {
    var date = new Date(this.valueOf());
    date.setDate(date.getDate() + days);
    return date;
}

function getDateFromDateString(dateString) {
    const year = dateString.substring(0, 4);
    const month = dateString.substring(4, 6);
    const day = dateString.substring(6, 8);
    return new Date(year, month-1, day)
}

function getEndDateFromStartDate(startDate, duration) {
    return new Date(startDate.addDays(duration))
}

function getDaysOfTheMonth(year, month) {
    return new Date(year, month, 0).getDate();
}

// Listener
function requestListener (req, res, callback) {
    res.setHeader('Content-Type', 'application/json');
    let body = '';
    req.on('data', chunk => {
        body += chunk.toString();
    });
    req.on('end', () => {
        callback(res, req, JSON.parse(body));
    })
}

const getPostBody = (res, req, body) => {
    let reqBody = body;
    
    // common attributes
    const article = body.article ? body.article : null;
    const project = body.project ? body.projet : 'en.wikipedia';
    const startDateString = body.startDateString ? body.startDateString : null;
    let start;
    let duration;
    let end;
    
    
    // Routing
    switch (req.url) {
        case "/":
            res.statusCode = 200;
            break

        case "/highDay":
            // day of the month where an article got the most views
            // required: article, start
            start = getDateFromDateString(startDateString);
            end = getEndDateFromStartDate(
                start,
                getDaysOfTheMonth(start.getFullYear(), start.getMonth()));

            pageviews.getPerArticlePageviews({
                article,
                project,
                start,
                end,
            }).then(wikiRes => {
                res.statusCode = 200;
                const highDay = wikiRes.items.reduce((prev, curr) => {
                    return curr.views > prev.views ? curr : prev
                })
                res.end(JSON.stringify(highDay, null, 2));  // pretty print
            }).catch(err => {
                console.log(`Error from wiki: ${err}`)
            });
            break

        case "/mostViewed":
            // list of most viewed articles for a month
            // n = number of articles
            // year YYYY
            // month MM
            // required: year, month

            const limit = body.limit ? body.limit : 10;
            const year = body.year ? body.year : null;
            const month = body.month ? body.month : null;
            const day = body.day ? body.day : 'all-days';
            
            pageviews.getTopPageviews({
                project,
                year,
                month,
                day,
                limit,
            }).then(wikiRes => {
                res.statusCode = 200;
                res.end(JSON.stringify(wikiRes, null, 2));  // pretty print
            }).catch(err => {
                console.log(`Error from wiki: ${err}`)
            });
            break

        case "/viewCount":
            // get view count for a week or month
            // required: article, start
            start = getDateFromDateString(startDateString);
            duration = 0;
            if (body.duration) {
                if (body.duration == 'weekly') {
                    duration = 7;
                } else if (body.duration == 'monthly') {
                    duration = getDaysOfTheMonth(start.getFullYear(), start.getMonth());
                }
            }
            end = getEndDateFromStartDate(start, duration);

            pageviews.getPerArticlePageviews({
                article,
                project,
                start,
                end,
            }).then(wikiRes => {
                res.statusCode = 200;
                res.end(JSON.stringify(wikiRes, null, 2));  // pretty print
            }).catch(err => {
                console.log(`Error from wiki: ${err}`)
            });
            break

        default:
            res.statusCode = 404;
            res.end("resource not found");
    }
}

// Server
const server = http.createServer((req, res) => {
    requestListener(req, res, getPostBody)
});

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});
