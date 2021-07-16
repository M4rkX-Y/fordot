using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System.IO;

public class Dialog : MonoBehaviour
{
    public Text textDisplay;
    public string[] sentences;
    private int index;
    public float typingSpeed;

    public GameObject DialogUI;

    private bool onetime = false;

    void Start(){
        DialogUI.SetActive(false);
    }


    void Update()
    {
        string json = File.ReadAllText(Application.dataPath + "/Script/api.json");
        //Debug.Log(json);
        apiData loadapiData = JsonUtility.FromJson<apiData>(json);
        //Debug.Log(loadapiData.tire_warning);
        if (!onetime){
            if (loadapiData.tire_warning){
                DialogUI.SetActive(true);
                dialogDisplay();
                onetime = true;
            }
        }
        
    }
    public void resume() {
        //Debug.Log("success");
        DialogUI.SetActive(false);
    }
    public void dialogDisplay(){
        StartCoroutine(Type());
    }

    IEnumerator Type(){
        foreach(char letter in sentences[index].ToCharArray()){
            textDisplay.text += letter;
            yield return new WaitForSeconds(typingSpeed);
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
