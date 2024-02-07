import { getDateFromDateString,
    getEndDateFromStartDate,
    getDaysOfTheMonth } from './../helpers.js';

test('convert a YYYYMMDD string to a js date', () => {
    // given
    const dateString = '20240229';
    const expectedDate = new Date(2024, 1, 29);
    // when date string is converted
    const receivedDate = getDateFromDateString(dateString);
    // then we receive a js date object
    // comparing dates to weird
    expect(receivedDate.getFullYear()).toBe(expectedDate.getFullYear());
    expect(receivedDate.getMonth()).toBe(expectedDate.getMonth());
    expect(receivedDate.getDay()).toBe(expectedDate.getDay());
});

test('get end date from start date given a duration', () => {
    // given
    const duration = 7;
    const startDate = new Date(2023, 11, 25);
    const expectedDate = new Date(2024, 0, 1);
    // when we calculate an end date with the duration
    const receivedDate = getEndDateFromStartDate(startDate, duration);
    // then we receive a new date, crossing months and years as we expect
    expect(receivedDate.getFullYear()).toBe(expectedDate.getFullYear());
    expect(receivedDate.getMonth()).toBe(expectedDate.getMonth());
    expect(receivedDate.getDay()).toBe(expectedDate.getDay());
});

test('get days of the month given any month and year', () => {
    // given
    const year = 2024;
    const month = 2;
    const expectedDays = 29;
    // when we check number of days
    const receivedDays = getDaysOfTheMonth(year, month);
    // then we receive the number, taking into account leap years
    expect(receivedDays).toBe(expectedDays);
});
