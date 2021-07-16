using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GameMenu : MonoBehaviour
{
    public static bool gp = false;

    public GameObject menuUI;


    void Start()
    {
        menuUI.SetActive(false);
    }

    void Update()
    {
        
    }

    public void pause() {
        menuUI.SetActive(true);
        gp = true;
    }


    public void resume() {
        //Debug.Log("success");
        menuUI.SetActive(false);
        gp = false;
    }
}
