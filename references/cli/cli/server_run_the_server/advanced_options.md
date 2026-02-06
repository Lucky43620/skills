# Server Configuration Options

## Database
*   `-d <db_name>`: Database to use.
*   `-i <modules>`: Install modules (comma-separated).
*   `-u <modules>`: Update modules.
*   `--db_host`: Database host.
*   `--db_port`: Database port.
*   `--db_user`: Database user.
*   `--db_password`: Database password.

## Advanced
*   `--dev=all`: Enable all developer features (reload, qweb debug, etc.).
*   `--workers`: Number of HTTP workers (for multiprocessing).
*   `--limit-time-real`: CPU time limit per request.

## Testing
*   `--test-enable`: Enable unit tests.
*   `--stop-after-init`: Stop server after loading/updating/testing.
