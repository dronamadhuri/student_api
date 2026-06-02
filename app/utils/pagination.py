def paginate(data, page=1, limit=5):

    start = (page - 1) * limit
    end = start + limit

    return data[start:end]