def greet(name):
    """Returns a greeting message."""
    if not name:
        return "Hello, World!"
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("Recruiter"))