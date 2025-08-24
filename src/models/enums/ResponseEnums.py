from enum import Enum

class responseSignal(Enum):

    FILE_VALIDATE_SUCCESS = "file_validate_successfly"
    FILE_TYPE_NOT_SUPPORTED = "file_type_not_supported"
    FILE_SIZE_EXCEEDED = "file_size_exceeded"
    FILE_UPLOAD_SUCCESS = "file_upload_success"
    FILE_UPLOAD_FAILED = "file_upload_failed"
    PROCESSING_FAILD = "processing_faild"
    PROCESSING_SUCCESS = "processing_success"