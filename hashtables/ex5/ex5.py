def finder(files, queries):
    cache = {}
    for q in queries: 
        cache[q]=True
        
    result = []
    
    for path in files:
        if path.split("/")[-1] in cache:
            result.append(path)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))