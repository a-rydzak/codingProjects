package com.example.brobofett.hauntedgranburry_2;

import android.media.MediaPlayer;
import android.os.Bundle;
import android.os.Handler;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.text.method.LinkMovementMethod;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.SeekBar;
import android.widget.TextView;
import android.widget.ViewFlipper;

import java.util.concurrent.TimeUnit;

public class Page8Activity extends AppCompatActivity {
    private ImageButton img_1, img_2, img_3, img_4,img_5;
    private ImageButton play_button;
    private ViewFlipper viewFlipper;
    private Button nextImage;
    private TextView songDuration;
    private int timeStart = 0, finalTime, timeMax, currentTime;
    private Handler durationHandler = new Handler();
    SeekBar progressBar;
    MediaPlayer mp;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_page8);

        //Button and clickable set up
        play_button = (ImageButton) findViewById(R.id.button);
        viewFlipper = (ViewFlipper) findViewById(R.id.viewFlipper);
        TextView t2 = (TextView) findViewById(R.id.text2);
        t2.setMovementMethod(LinkMovementMethod.getInstance());
        mp = MediaPlayer.create(this, R.raw.sound);
        progressBar = (SeekBar) findViewById(R.id.progressBar);
        songDuration = (TextView) findViewById(R.id.tt);
        img_1= (ImageButton) findViewById(R.id.img1);
        img_2= (ImageButton) findViewById(R.id.img2);
        img_3= (ImageButton) findViewById(R.id.img3);
        img_4= (ImageButton) findViewById(R.id.img4);
//        img_5= (ImageButton) findViewById(R.id.img5);
//
//
        //Media Player set up
        progressBar.setProgress(0);
        progressBar.setMax(mp.getDuration());
        finalTime=mp.getDuration();
        songDuration.setText(String.format("%d min, %d sec", TimeUnit.MILLISECONDS.toMinutes((long)  (finalTime-mp.getCurrentPosition())), TimeUnit.MILLISECONDS.toSeconds((long)  (finalTime-mp.getCurrentPosition())) - TimeUnit.MINUTES.toSeconds(TimeUnit.MILLISECONDS.toMinutes((long)  (finalTime-mp.getCurrentPosition())))));


        //Set View Flipper to flip through images
        img_1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                viewFlipper.showNext();
            }
        });
        img_2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                viewFlipper.showNext();
            }
        });
        img_3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                viewFlipper.showNext();
            }
        });
        img_4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                viewFlipper.showNext();
            }
        });
//        img_5.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                viewFlipper.showNext();
//            }
//        });
        //Runnable thread that syncs the seek bar to the mp3 file
        Runnable updateSeekBarTime = new Runnable() {
            public void run() {

                progressBar.setProgress((int) mp.getCurrentPosition());
                durationHandler.postDelayed(this, 100);

            }
        };

        Thread thread = new Thread(updateSeekBarTime);
        thread.start();
//
        //Set up on click listener to react when playbutton is pressed

        play_button.setOnClickListener(new View.OnClickListener() {
            public void onClick(View view) {


                if (mp.isPlaying()) {
                    mp.pause();
                    progressBar.setProgress(mp.getCurrentPosition());
                    play_button.setImageDrawable(
                            ContextCompat.getDrawable(getApplicationContext(), R.mipmap.play));
//                    play_button.setText("Paused");
                } else {
                    mp.start();
                    play_button.setImageDrawable(
                            ContextCompat.getDrawable(getApplicationContext(), R.mipmap.pause));
//                    play_button.setBackgroundResource(R.mipmap.pause);

                }
            }
        });


        progressBar.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser) {
                songDuration.setText(String.format("%d min, %d sec", TimeUnit.MILLISECONDS.toMinutes((long)  (finalTime-mp.getCurrentPosition())), TimeUnit.MILLISECONDS.toSeconds((long)  (finalTime-mp.getCurrentPosition())) - TimeUnit.MINUTES.toSeconds(TimeUnit.MILLISECONDS.toMinutes((long)  (finalTime-mp.getCurrentPosition())))));
            }

            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {




            }

            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {
                mp.seekTo(progressBar.getProgress());
                songDuration.setText(String.format("%d min, %d sec", TimeUnit.MILLISECONDS.toMinutes((long)  (finalTime-mp.getCurrentPosition())), TimeUnit.MILLISECONDS.toSeconds((long)  (finalTime-mp.getCurrentPosition())) - TimeUnit.MINUTES.toSeconds(TimeUnit.MILLISECONDS.toMinutes((long)  (finalTime-mp.getCurrentPosition())))));
            }
        });



    }

    //Stops the audio player whenever the activity is stopped/ user leaves the activity
    @Override
    protected void onStop() {
        // call the superclass method first
        super.onStop();
        Runtime.getRuntime().gc();
        mp.stop();
    }

    //This is to set memory null for storage purposes, I do not know if this actially works.
    @Override
    protected void onDestroy() {
        //android.os.Process.killProcess(android.os.Process.myPid());

        super.onDestroy();
        if(viewFlipper!=null)
        {
            viewFlipper=null;
        }

    }

}