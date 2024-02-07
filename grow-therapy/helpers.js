// Helper methods
Date.prototype.addDays = function(days) {
    const date = new Date(this.valueOf());
    date.setDate(date.getDate() + days);
    return date;
}

export function getDateFromDateString(dateString) {
    const year = dateString.substring(0, 4);
    const month = dateString.substring(4, 6);
    const day = dateString.substring(6, 8);
    return new Date(year, month-1, day)
}

export function getEndDateFromStartDate(startDate, duration) {
    return new Date(startDate.addDays(duration))
}

export function getDaysOfTheMonth(year, month) {
    return new Date(year, month, 0).getDate();
}
