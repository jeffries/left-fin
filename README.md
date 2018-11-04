# Nemo: Personal Financial Manager

Nemo helps individuals manage their finances. It has some handy features, including:
- Multiple account support
- Tracking money owed by or to you
- Multiple currency support\
- Budgeting

This project is split into two components: `nemo` and `marlin`; these are the backend and frontend, respectively, and are written in Python and JavaScript, respectively.

This project is built as one big Docker image, including the backend and frontend.

## Running

```
make dev # Run development server
```

## Building

```
make image # build a production Docker image
```

## Testing

Tests are located in the `tests/nemo/` directory for the Python backend, and `tests/marlin/` for the JavaScript frontend.

```
make test # Run unit tests
```
