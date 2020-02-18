def paginate(req, resp, resource, params, default=10):

    start = int(req.params['start']) if 'start' in req.params else None

    end = int(req.params['end']) if 'end' in req.params else None

    if (start and end):
        req.paginate = [start, end]
    else:
        req.paginate = [1, 1+default]
