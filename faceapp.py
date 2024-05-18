import tkinter as tk
from tkhtmlview import HTMLLabel

class FaceRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition App")
        self.root.geometry("800x600")

        # Load and display HTML content
        self.render_html()

    def render_html(self):
        # Define the HTML content
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Sliding Form</title>
            <link rel="stylesheet" href="style.css">
        </head>
        <body>
            <div class="container" id="container">
                <!-- Your HTML content here -->
            </div>

            <script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
            <script src="script.js"></script>
            <script>
                document.addEventListener("DOMContentLoaded", function() {
                    const signUpButton = document.getElementById("signUp");
                    const signInButton = document.getElementById("signIn");
                    const container = document.getElementById("container");

                    signUpButton.addEventListener("click", () => {
                        container.classList.add("right-panel-active");
                    });

                    signInButton.addEventListener("click", () => {
                        container.classList.remove("right-panel-active");
                    });
                });
            </script>
        </body>
        </html>
        """

        # Create HTMLLabel widget and pack it into the root window
        html_label = HTMLLabel(self.root, html=html_content)
        html_label.pack(expand=True, fill='both')

if __name__ == "__main__":
    root = tk.Tk()
    app = FaceRecognitionApp(root)
    root.mainloop()
