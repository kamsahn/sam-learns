const http = require('http');
const server = require('./server.js');

afterAll(() => {
    server.close()
});

test('server should work', () => {
    expect(server.getDaysOfTheMonth(2024, 2)).toBe(29);
});
