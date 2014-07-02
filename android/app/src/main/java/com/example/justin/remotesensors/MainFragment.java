package com.example.justin.remotesensors;

import android.app.Fragment;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.TextView;

/**
 * Created by Justin on 6/30/2014.
 */



public class MainFragment extends Fragment implements View.OnClickListener {
    private Button clicker;
    private TextView text;

    public MainFragment() {

    }
    /*
     *This function gets called once the initial layout of android is generated. It runs in the background
     *and waits for the button to be clicked. The button will call a function that sends http request
     *with the GET method to the REST interface at the url below. The function will return a string with
     *the raw data from the MongoDB server being hosted and will post that data in the textview text box
     */
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View rootView = inflater.inflate(R.layout.fragment_main, container, false);
        clicker = (Button)rootView.findViewById(R.id.requests);
        text = (TextView)rootView.findViewById(R.id.results);
        clicker.setOnClickListener(this);
        return rootView;
    }

    public void refreshText(String response) {
        text.setText(response);
    }

    @Override
    public void onClick(View view) {
        new RequestTask(this).execute("https://dsp-csci-project.cloud.dreamfactory.com/rest/mongodb/sensordata?app_name=TEST&limit=10");
    }
}
