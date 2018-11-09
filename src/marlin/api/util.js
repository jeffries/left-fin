/**
 * Multi-level request construction. Returns a Promise from fetch().
 * 
 * The multi-level setup allows incremental construction of endpoints.
 * 
 * buildAPI('http://google.com')('GET', '/search')({ q: 'planes' }) => 
 *     fetch('http://google.com/search?q=planes', { method: 'GET' })
 * @param {*} baseURL 
 */
export const buildAPI = baseURL => (method, path) => body => {
    let opts = { method: method };
    let query;
    let url;

    switch (method) {
        case 'POST':
            opts.body = body;
            break;
        case 'GET':
            if (body) throw 'oops';
            break;
    }

    if (query) {
        url = baseURL + path + '?' + query;
    }
    else {
        url = baseURL + path;
    }

    return fetch(url, opts);
};