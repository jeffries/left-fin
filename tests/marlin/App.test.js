import React from 'react';
import App from 'Components/App';
import TestRenderer from 'react-test-renderer';

test('renders without crashing', () => {
    const a = TestRenderer.create(
        <App />
    ).toJSON();
    expect(a).toBeTruthy();
});
