from fastapi import APIRouter


router = APIRouter()


@router.get("/asdf", tags=["API"])
def root():
    """
    Root of host
    """
    output = {
        'message': 'FastAPI API'
    }
    return output
