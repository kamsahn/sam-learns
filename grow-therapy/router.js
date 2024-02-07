import pageviews from 'pageviews';

import { getDateFromDateString,
    getEndDateFromStartDate,
    getDaysOfTheMonth } from './helpers.js';

function router(res, req, body) {
    // common attributes
    const article = body.article ? body.article : null;
    const project = body.project ? body.project : 'en.wikipedia';
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
            // required: article, startDateString
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
            // required: year (YYYY), month (MM)
            // optional: day (DD or 'all-days'), limit

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
            // required: article, startDateString
            // optional: duration ('monthly' or 'weekly')
            start = getDateFromDateString(startDateString);
            duration = 0;
            if (body.duration) {
                if (body.duration === 'weekly') {
                    duration = 7;
                } else if (body.duration === 'monthly') {
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
            res.end('resource not found');
    }
}

export default router
