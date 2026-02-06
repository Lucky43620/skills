# Extract API Routes

## Parse
**Route:** `/api/extract/parse`
**Method:** POST
**Params:**
*   `account_token`: Your IAP token.
*   `files`: List of base64 encoded files.

## Get Results
**Route:** `/api/extract/get_result`
**Method:** POST
**Params:**
*   `request_id`: ID returned by the parse call.

## Validation
**Route:** `/api/extract/validate`
**Method:** POST
Used to send user corrections back to the AI to improve future learning.
