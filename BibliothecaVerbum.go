package main

import (
	"net/http"

	"github.com/mozillazg/request"
	// "github.com/WAY29/icecream-go/icecream"
)

func main() {
	c := new(http.Client)
	req := request.NewRequest(c)
	resp, err := req.Get("http://httpbin.org/get")
	if err != nil {
		print("I'm sorry, there was an error while sending the request or recieving the response")
		print(err)
		err = nil
	}
	j, err := resp.Json()
	if err != nil {
		print("I'm sorry, there was an error while turning the response into JSON")
		print(err)
	}
	something, err := j.Get("headers").Get("Host").String()
	print(something)
	defer resp.Body.Close()
}
