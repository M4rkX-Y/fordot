using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;
public class Character_grow : MonoBehaviour
{

    public float speed = 1f;
    public float delay = 4.5f;
    public float bsize = 1f;
    private int stop = 0;
    private float time;
    private bool up = true;
    public Vector2 t;
    public Vector2 f;
    public Vector2 b;
    public Vector2 s;
    private string check;
    private bool onetime = false;

    // Start is called before the first frame update
    void Start()
    {
        f = transform.localScale;
        b.x = f.x + bsize;
        b.y = f.x + bsize;
    }

    // Update is called once per frame
    void Update()
    {
        
        string json = File.ReadAllText(Application.dataPath + "/Script/api.json");
        Debug.Log(json);
        apiData loadapiData = JsonUtility.FromJson<apiData>(json);
        check = loadapiData.ignition_status;

        time = delay/transform.localScale.x;
        if (stop==0) {
            Invoke("stay", time);            
        }
        
        if (stop==1) {
            Invoke("big", time);            
        }

        if (stop==2) {
            Invoke("small", time);
        }
        
        

        if (Input.GetKeyUp("escape")) {
            b.x = f.x + bsize;
            b.y = f.x + bsize;
            stop = 0;
        }

        if (Input.GetKeyUp("space")) {
            stop = 1;
        }

        if (Input.GetKeyUp(KeyCode.Return)) {
            stop = 2;
        }

        if (!onetime){
            if (check == "ON") {
            stop = 2;
            onetime = true;
            }
        }


            
    }
    void big(){
        t = transform.localScale;
        if (t.x < 5) {
            t.x += Time.deltaTime * speed;
            t.y += Time.deltaTime * speed;
            transform.localScale = t;
        }
    }
    void stay(){
        f = transform.localScale;
        transform.localScale = f;

            
    }
    void small(){
        s = transform.localScale;
        if (s.x > 2) {
            s.x += Time.deltaTime * speed * -1;
            s.y += Time.deltaTime * speed * -1;
            transform.localScale = s;
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
        public bool charge_plug_value;
    }
}
