package com.example.brobofett.hauntedgranburry_2;

import android.Manifest;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.location.Location;
import android.location.LocationListener;
import android.os.Build;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.annotation.RequiresApi;
import android.support.v4.app.FragmentActivity;
import android.support.v4.content.ContextCompat;
import android.view.View;
import android.widget.ImageButton;

import com.google.android.gms.common.ConnectionResult;
import com.google.android.gms.common.api.GoogleApiClient;
import com.google.android.gms.maps.CameraUpdate;
import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.BitmapDescriptorFactory;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;

import static com.example.brobofett.hauntedgranburry_2.R.id.map;

public class Navigation extends FragmentActivity implements OnMapReadyCallback,
        GoogleApiClient.ConnectionCallbacks, GoogleApiClient.OnConnectionFailedListener, LocationListener {

    private GoogleMap mMap;
    private GoogleApiClient mGoogleApiClient;
    private ImageButton button1, button3, button4 , button5, button6, button7,button8, button9,button10;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_navigation);

        //THIS STARTS THE REVIEW


        // Obtain the SupportMapFragment and get notified when the map is ready to be used.
        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager()
                .findFragmentById(map);
        mapFragment.getMapAsync(this);

        button1 = (ImageButton) findViewById(R.id.img1);
        button3 = (ImageButton) findViewById(R.id.img3);
        button4 = (ImageButton) findViewById(R.id.img4);
        button5 = (ImageButton) findViewById(R.id.img5);
        button6 = (ImageButton) findViewById(R.id.img6);
        button7 = (ImageButton) findViewById(R.id.img7);
        button8 = (ImageButton) findViewById(R.id.img8);
        button9 = (ImageButton) findViewById(R.id.img9);
        button10 = (ImageButton) findViewById(R.id.imgAp);


        button1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                firstButtonPage();
            }
        });


        button3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                thirdButtonPage();
            }
        });
        button4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                fourthButtonPage();
            }
        });
        button5.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                fifthButtonPage();
            }
        });
        button6.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                sixthButtonPage();
            }
        });
        button7.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                seventhButtonPage();
            }
        });
        button8.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                eighthButtonPage();
            }
        });
        button9.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                ninthButtonPage();
            }
        });
        button10.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                tenthButtonPage();
            }
        });
    }


    private void firstButtonPage() {
        Intent intent1 = new Intent(this, Page1Activity.class);
        startActivity(intent1);
    }

    private void thirdButtonPage() {
        Intent intent3 = new Intent(this, Page3Activity.class);
        startActivity(intent3);
    }
    private void fourthButtonPage() {
        Intent intent4 = new Intent(this, Page4Activity.class);
        startActivity(intent4);
    }
    private void fifthButtonPage() {
        Intent intent5 = new Intent(this, Page5Activity.class);
        startActivity(intent5);
    }
    private void sixthButtonPage() {
        Intent intent6= new Intent(this, Page6Activity.class);
        startActivity(intent6);
    }
    private void seventhButtonPage() {
        Intent intent7 = new Intent(this, Page7Activity.class);
        startActivity(intent7);
    }
    private void eighthButtonPage() {
        Intent intent8 = new Intent(this, Page8Activity.class);
        startActivity(intent8);
    }
    private void ninthButtonPage() {
        Intent intent9 = new Intent(this, Page9Activity.class);
        startActivity(intent9);
    }
    private void tenthButtonPage() {
        Intent intent10 = new Intent(this, AppreciationActivity.class);
        startActivity(intent10);
    }

    /**
     * Manipulates the map once available.
     * This callback is triggered when the map is ready to be used.
     * This is where we can add markers or lines, add listeners or move the camera. In this case,
     * we just add a marker near Sydney, Australia.
     * If Google Play services is not installed on the device, the user will be prompted to install
     * it inside the SupportMapFragment. This method will only be triggered once the user has
     * installed Google Play services and returned to the app.
     */



    @RequiresApi(api = Build.VERSION_CODES.M)
    @Override
    public void onMapReady(GoogleMap googleMap) {
        mMap = googleMap;

        if (ContextCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION)
                == PackageManager.PERMISSION_GRANTED) {
            mMap.setMyLocationEnabled(true);
        } else {

        }

        // Locations Placed Here

        LatLng jailhouse = new LatLng(32.44363, -97.78647);
        LatLng courthouse = new LatLng(32.442665 , -97.787054);
        LatLng nuttHouse= new LatLng(32.443344, -97.786624);
        LatLng langdonCenter= new LatLng(32.442339, -97.784870);
        LatLng operaHouse= new LatLng(32.442037, -97.786731);
        LatLng nutshellBakery= new LatLng(32.442009, -97.786580);
        LatLng cemetery= new LatLng(32.452678, -97.785817);
        LatLng townWest= new LatLng(32.442649, -97.787835);

        // Markers Added Here
        mMap.addMarker(new MarkerOptions().position(jailhouse).title("Hood County Jailhouse").icon(BitmapDescriptorFactory.fromResource(R.drawable.darcula1)));
        mMap.addMarker(new MarkerOptions().position(courthouse).title("Hood County Courthouse").icon(BitmapDescriptorFactory.fromResource(R.drawable.darcula2)));
        mMap.addMarker(new MarkerOptions().position(nuttHouse).title("Nutt House Hotel / Ghosts and Legends Tour").icon(BitmapDescriptorFactory.fromResource(R.drawable.darcula3)));
        mMap.addMarker(new MarkerOptions().position(langdonCenter).title("Langdon Center").icon(BitmapDescriptorFactory.fromResource(R.drawable.darcula4)));
        mMap.addMarker(new MarkerOptions().position(operaHouse).title("Granbury Opera House").icon(BitmapDescriptorFactory.fromResource(R.drawable.darcula5)));
        mMap.addMarker(new MarkerOptions().position(nutshellBakery).title("Nutshell Eatery and Bakery").icon(BitmapDescriptorFactory.fromResource(R.drawable.darcula6)));
        mMap.addMarker(new MarkerOptions().position(cemetery).title("Granbury Cemetery").icon(BitmapDescriptorFactory.fromResource(R.drawable.darcula7)));
        mMap.addMarker(new MarkerOptions().position(townWest).title("Market On the Square").icon(BitmapDescriptorFactory.fromResource(R.drawable.darcula8)));
        //Animate Map Camera Location
        CameraUpdate center= CameraUpdateFactory.newLatLng(new LatLng(32.44363, -97.78647));
        CameraUpdate zoom=CameraUpdateFactory.zoomTo(16);
        mMap.moveCamera(center);
        mMap.animateCamera(zoom);

    }

    private void shouldShowRequestPermissionRationale(boolean b) {
    }

    @Override
    public void onLocationChanged(Location location) {

    }

    @Override
    public void onStatusChanged(String provider, int status, Bundle extras) {

    }

    @Override
    public void onProviderEnabled(String provider) {

    }

    @Override
    public void onProviderDisabled(String provider) {




    }

    @Override
    public void onConnectionFailed(@NonNull ConnectionResult connectionResult) {

    }

    @Override
    public void onConnected(@Nullable Bundle bundle) {

    }

    @Override
    public void onConnectionSuspended(int i) {

    }
}
