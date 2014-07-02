package com.example.justin.remotesensors;

import android.util.Log;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

/**
 * Created by Justin on 6/30/2014.
 */
public class JSONParser {
    private static final String TAG_RECORD = "record";
    private static final String TAG_NAME = "boardName";
    private static final String TAG_ID = "_id";
    private static final String TAG_SENSORDATA = "sensorData";
    private static final String TAG_LIGHT = "Light";
    private static final String TAG_TEMP = "Temperature";
    private static final String TAG_DATE = "date";

    public static JSONObject textToJSON(String input) {
        // try parse the string to a JSON object
        JSONObject jobj = null;
        try {
            jobj = new JSONObject(input);
        } catch (JSONException e) {
            Log.e("JSON Parser", "Error parsing data " + e.toString());
        }

        return jobj;
    }

    public static JSONObject parseJSON(JSONObject json) {
        try {
            JSONArray records = json.getJSONArray(TAG_RECORD);
            for (int i = 0; i < records.length(); i++) {
                JSONObject r = records.getJSONObject(i);
                String boardName = r.getString(TAG_NAME);
                String id = r.getString(TAG_ID);
                JSONArray sensors = r.getJSONArray(TAG_SENSORDATA);
                for (int j = 0; j < sensors.length(); i++) {

                }
            }
        } catch (JSONException e) {

        }
    }
}
