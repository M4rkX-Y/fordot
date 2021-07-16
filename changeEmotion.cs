using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;

public class changeEmotion : MonoBehaviour
{
    public Animator animator;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        string json = File.ReadAllText(Application.dataPath + "/Script/api.json");
        //Debug.Log(json);
        apiData loadapiData = JsonUtility.FromJson<apiData>(json);
        if (loadapiData.tire_warning){
            animator.SetBool("Emotion", false);
        }
        else {
            animator.SetBool("Emotion", true);
        }
    }
    private class apiData{
        public int fuel_value;
        public int fuel_distance_to_empty;
        public string location_longitude;
        public string location_latitude;
        public int speed;
        public string direction;
        public string door_unspecified_front_door;
        public string door_unspecified_front_role;
        public string engine_status;
        public int engine_duration;
        public bool tire_warning;
        public string charge_value;
        public string charge_start;
        public string charge_end;
        public string ignition_status;
        public bool battery_value;
        public int battery_distanceToEmpty;
        public int mileage;
        public int odometer;
        public bool milecharge_plug_valueage;
        
    }
}
