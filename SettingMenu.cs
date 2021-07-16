using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System.IO;

public class SettingMenu : MonoBehaviour
{

    public GameObject menuUI;


    public string VID;
    public string DM;
    public string TK;

    void Start()
    {
        menuUI.SetActive(false);
    }


    public void pause() {
        menuUI.SetActive(true);
    }



    public void getVID(string s){
        VID = s;
        Debug.Log(VID);
    }
    public void getDM(string s){
        DM = s;
    }
    public void getTK(string s){
        TK = s;
    }
    
    public void resume() {
        userInfo newinfo = new userInfo();
        newinfo.vehicle_id = VID;
        newinfo.token = DM;
        newinfo.domain = TK;
        string json = JsonUtility.ToJson(newinfo);
        Debug.Log(json);
        File.WriteAllText(Application.dataPath + "/Script/token.json", json);
        menuUI.SetActive(false);
    }

    public void exit(){
        menuUI.SetActive(false);
    }

    public class userInfo {
        public string vehicle_id;
        public string token;
        public string domain;

    }
}
