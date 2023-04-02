// Make a simple GO web server that serves the html files from  /templates, static files from /static, and the .ico file from /static. Also make a login function using prisma-client-go@latest.

package main

import (
	"fmt"
	"html/template"
	"log"
	"net/http"
	"os"

	"github.com/gorilla/mux"

	"github.com/prisma/prisma-client-go"
)


func main() {
	// Create a new router
	r := mux.NewRouter()

	// Serve static files
	fs := http.FileServer(http.Dir("./static"))
	r.PathPrefix("/static/").Handler(http.StripPrefix("/static/", fs))

	// Serve favicon
	favicon := http.FileServer(http.Dir("./static"))
	r.PathPrefix("/favicon.ico").Handler(http.StripPrefix("/favicon.ico", favicon))

	// Serve html files
	r.HandleFunc("/", indexHandler)
	r.HandleFunc("/login", loginHandler)

	// Start the server
	fmt.Println("Server is listening on port 8080")
	log.Fatal(http.ListenAndServe(":8080", r))
}

func indexHandler(w http.ResponseWriter, r *http.Request) {
	tmpl := template.Must(template.ParseFiles("templates/index.html"))
	tmpl.Execute(w, nil)
}

func loginHandler(w http.ResponseWriter, r *http.Request) {
	// Create a new Prisma Client
	client := prisma.New(nil)

	// Get the email and password from the form
	email := r.FormValue("email")
	password := r.FormValue("password")

	// Find the user in the database
	user, err := client.User.FindUnique(prisma.User.Email.Equals(email)).Exec(context.Background())
	if err != nil {
		fmt.Println(err)
	}

	// Check if the password is correct
	if user.Password == password {
		fmt.Println("Logged in")
	} else {
		fmt.Println("Wrong password")
	}
}

// Path: index.html
// Make a simple html form that sends a POST request to /login.

<!DOCTYPE html>
<html>
<head>
	<title>Prisma Client Go</title>
</head>
<body>
	<form action="/login" method="POST">
		<input type="email" name="email" placeholder="Email">
		<input type="password" name="password" placeholder="Password">
		<button type="submit">Login</button>
	</form>
</body>
</html>

