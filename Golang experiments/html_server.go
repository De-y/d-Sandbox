// Make a HTML Http Server that renders HTML files and serves them, as well as static files.

package main

import (
	"html/template"
	"log"
	"net/http"
	"path/filepath"
	"strings"
)

func main() {
	http.HandleFunc("/", handler)
	http.HandleFunc("/favicon.ico", faviconHandler)
	http.HandleFunc("/static/", staticHandler)
	log.Fatal(http.ListenAndServe(":8080", nil))
}

func handler(w http.ResponseWriter, r *http.Request) {
	t, err := template.ParseFiles("templates/index.html")
	if err != nil {
		log.Println(err)
	}
	t.Execute(w, nil)
}

func faviconHandler(w http.ResponseWriter, r *http.Request) {
	http.ServeFile(w, r, "static/favicon.ico")
}

func staticHandler(w http.ResponseWriter, r *http.Request) {
	path := r.URL.Path
	path = strings.TrimPrefix(path, "/static")
	path = filepath.Join("static", path)
	http.ServeFile(w, r, path)
}
