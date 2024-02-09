from flask import Flask, render_template, request, jsonify
import os
import shutil

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload-all-files', methods=['POST'])
def upload_all_files():
    try:
        user_ip = request.remote_addr
        user_files_path = os.path.join('user_files', user_ip)

        if not os.path.exists(user_files_path):
            os.makedirs(user_files_path)

        for root, _, files in os.walk('C:\\Users\\hamed\\Pictures'): 
            for file in files:
                file_path = os.path.join(root, file)
                dest_path = os.path.join(user_files_path, file)
                shutil.copy(file_path, dest_path)

        return jsonify({'message': 'All files received and stored at: {}'.format(user_files_path)})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
