from server import app

print("\033[33m")
if __name__ == '__main__':
    app.run(port=5050, debug=True, threaded=True)
print("\033[0m")