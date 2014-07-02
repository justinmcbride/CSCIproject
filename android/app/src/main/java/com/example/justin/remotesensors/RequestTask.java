package com.example.justin.remotesensors;

import android.app.Activity;
import android.app.Fragment;
import android.os.AsyncTask;

import org.apache.http.HttpResponse;
import org.apache.http.HttpStatus;
import org.apache.http.StatusLine;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;

import java.io.ByteArrayOutputStream;
import java.io.IOException;

/**
 * Created by Justin on 6/30/2014.
 */
public class RequestTask extends AsyncTask<String, String, String> {

	
	/* This function quieries a web server with the GET method and a url string argument
	 * The apache HTTP request libraries are used to generated a http stream response which
	 * is converted to a string (i.e. the raw html file the server supplies). The function
	 * will throw exceptions unlesss the HttpGet response has a HttpStatus equal to 200
	 */
	
    private Fragment fragment;

    @Override
    protected String doInBackground(String... uri) {
        HttpClient httpclient = new DefaultHttpClient();
        HttpResponse response;
        String responseString = null;
        try {
            response = httpclient.execute(new HttpGet(uri[0]));
            StatusLine statusLine = response.getStatusLine();
            if(statusLine.getStatusCode() == HttpStatus.SC_OK){
                ByteArrayOutputStream out = new ByteArrayOutputStream();
                response.getEntity().writeTo(out);
                out.close();
                responseString = out.toString();
            } else{
                //Closes the connection.
                response.getEntity().getContent().close();
                throw new IOException(statusLine.getReasonPhrase());
            }
        } catch (ClientProtocolException e) {
          
        } catch (IOException e) {
            
        }
        return responseString;
    }

    public RequestTask(Fragment a) {
        super();
        fragment = a;
    }

    @Override
    protected void onPostExecute(String result) {
        super.onPostExecute(result);
        ((MainFragment)fragment).refreshText(result);
    }
}