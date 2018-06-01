package com.example.brobofett.hauntedgranburry_2;

import android.Manifest;
import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;
import android.os.Bundle;
import android.support.v4.app.ActivityCompat;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.view.Gravity;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    private Button startTourButton;
    private TextView text;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        startTourButton = (Button) findViewById(R.id.startTourButton);
        startTourButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startTour();
            }
        });

        if (ContextCompat.checkSelfPermission(this,
                Manifest.permission.ACCESS_FINE_LOCATION)
                != PackageManager.PERMISSION_GRANTED) {

            // Should we show an explanation?
            if (ActivityCompat.shouldShowRequestPermissionRationale(this,
                    Manifest.permission.ACCESS_FINE_LOCATION)) {

                // Show an explanation to the user *asynchronously* -- don't block
                // this thread waiting for the user's response! After the user
                // sees the explanation, try again to request the permission.

            } else {

                // No explanation needed, we can request the permission.

                ActivityCompat.requestPermissions(this,
                        new String[]{Manifest.permission.ACCESS_FINE_LOCATION},
                        1);

                // MY_PERMISSIONS_REQUEST_READ_CONTACTS is an
                // app-defined int constant. The callback method gets the
                // result of the request.
            }
        }

        ///////////////////Checks for connection to WiFi or Mobile data and asks user to activate it to use map

        ConnectivityManager cm = (ConnectivityManager)this.getSystemService(Context.CONNECTIVITY_SERVICE);
        NetworkInfo activeNetwork = cm.getActiveNetworkInfo();
        boolean isConnected = activeNetwork != null &&
                activeNetwork.isConnectedOrConnecting();

       if(!isConnected ) {
//           Toast.makeText(this, "Enable Mobile Data or WiFi Now For Map", Toast.LENGTH_LONG).show();
           Toast toast= Toast.makeText(this,
                   "Enable Mobile Data or WiFi Now For Map", Toast.LENGTH_LONG);
           toast.setGravity(Gravity.CENTER|Gravity.CENTER_HORIZONTAL, 0, 0);
           toast.show();

       }


    }

    private void startTour() {
        Intent intent= new Intent(this,Navigation.class);
        startActivity(intent);

    }


    }



