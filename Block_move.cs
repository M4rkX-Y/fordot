using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;

public class Block_move : MonoBehaviour
{
    // Start is called before the first frame update
    private Vector2 t;
    private bool onetime = false;
    private string check;

    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {

        string json = File.ReadAllText(Application.dataPath + "/Script/api.json");
        Debug.Log(json);
        apiData loadapiData = JsonUtility.FromJson<apiData>(json);
        check = loadapiData.ignition_status;
        t = new Vector2(0.0f, 0.0f);

        if (Input.GetKeyUp("space")) {
            in_water();
        }
     
        if (Input.GetKeyUp(KeyCode.Return)) {
            out_water();
        }

        if (!onetime){
            if (check == "ON") {
            out_water();
            onetime = true;
            }
        }
    }
    void in_water() {
        t.y += -3;
        transform.position = t;
    }
    void out_water() {
        t.y += 4;
        transform.position = t;
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
