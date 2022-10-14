from fastapi import HTTPException, Request


def verify_token(req: Request):
    token = req.headers.get("Authorization", None)
    valid = token == "BestPossiblePassword"
    if not valid:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return True
