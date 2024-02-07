import router from './../router.js';

test('can access home', () => {
    // given
    const mockRes = jest.fn();
    const mockReq = jest.fn();
    const mockBody = jest.fn();
    mockReq.url = "/";
    // when we are accessing the home route
    router(mockRes, mockReq, mockBody)
    // then we get a 200 status
    expect(mockRes.statusCode).toBe(200);
});

test('defaults to 404', () => {
    // given
    const mockRes = jest.fn();
    const mockReq = jest.fn();
    const mockBody = jest.fn();
    mockRes.end = jest.fn();
    mockReq.url = "/badRoute";
    // when we try to access a route that doesn't exist
    router(mockRes, mockReq, mockBody);
    // then we get a 404 status
    expect(mockRes.statusCode).toBe(404);
    expect(mockRes.end).toBeCalledWith('resource not found');
});
