package com.example.myapplication

import android.os.Bundle
import android.os.StrictMode
import android.text.method.ScrollingMovementMethod
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import okhttp3.*
import java.io.IOException


class MainActivity : AppCompatActivity() {


    private lateinit var responseTextView: TextView
    private lateinit var idTextEdit: EditText
    private lateinit var xPosition: EditText
    private lateinit var yPosition: EditText
    private lateinit var status: EditText

    private val client = OkHttpClient()
    // per potersi interfacciare con il server quest'ultimo deve girare su un ip raggiungibile dal telefono.
    // Io l'ho messo sul'ip del computer nella rete locale
    // Se lo si lascia sul default localhost, non è raggiungbile dal telefono
    // (django da errore se lo si mette su un ip diverso da localhost (127.0.0.1). Per farlo andare bisogna quindi modificare il file settings.py
    // Bisogna aggiungere a ALLOWED_HOSTS l'ip che si vuole usare tra virgolette, per esempio ALLOWED_HOSTS = ["192.168.0.102"])
    val url = "http://192.168.0.102:8000/workstation/"
    //questo qua sotto lo uso solo per il testing. Se lo si vuole usare prima avviare un server a quell'url che esponga un file json (con contenuto che non sia jsonArray)
    //val url = "http://192.168.0.102:8001/temp.json"

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)



        //per adesso metto questo StrictMode per non ricevere errori ma non sarebbe giusto
        //val policy = StrictMode.ThreadPolicy.Builder().permitAll().build()
        //StrictMode.setThreadPolicy(policy)

        responseTextView = findViewById<TextView>(R.id.responseText)
        idTextEdit = findViewById<EditText>(R.id.workstationIdEdit)
        xPosition = findViewById<EditText>(R.id.positionX)
        yPosition = findViewById<EditText>(R.id.positionY)
        status = findViewById<EditText>(R.id.workstationState)

        //rendo il resposneTextView scrollabile orizzontalmente
        // (oltra al comando seguente serve anche aver messo scrollbars - vertical = true per il responseTextView in activity_main.xml
        responseTextView.setMovementMethod(ScrollingMovementMethod())

        //per ogni pulsante assegna un onClickListener
        findViewById<Button>(R.id.getBtn).setOnClickListener {
            getRequest()
        }

        findViewById<Button>(R.id.postBtn).setOnClickListener {
            postRequest()
        }

        findViewById<Button>(R.id.deleteBtn).setOnClickListener {
            deleteRequest()
        }



    }

    private fun getRequest(){
        val request = Request.Builder()
                .url(url)
                .build()

        client.newCall(request).enqueue(object : Callback {
            override fun onFailure(call: Call, e: IOException) {}
            //scrivo il risultato sul responseTextView
            override fun onResponse(call: Call, response: Response) = writeToResponseTextView(response.body()!!.string())
        })
    }


    private fun postRequest(){
        val JSON = MediaType.parse("application/json; charset=utf-8")
        val json ="""
            {
                "WorkstationId": "${ idTextEdit.text }",
                "Xposition": "${ xPosition.text }",
                "Yposition": "${ yPosition.text }",
                "Status": "${ status.text }"
            }
        """.trimIndent()
        println(json)

        val body: RequestBody = RequestBody.create(JSON, json)
        val request = Request.Builder()
                .url(url)
                .post(body)
                .build()

        client.newCall(request).enqueue(object : Callback {
            override fun onFailure(call: Call, e: IOException) {}
            //scrivo il risultato sul responseTextView
            override fun onResponse(call: Call, response: Response) = writeToResponseTextView(response.body()!!.string())
        })
    }

    private fun deleteRequest(){
        val request = Request.Builder()
                .url(url+idTextEdit.text ) //aggiungo in fondo all'url l'id della postazione da eliminare, perché l'API accetta questo formato
                .delete()
                .build()

        client.newCall(request).enqueue(object : Callback {
            override fun onFailure(call: Call, e: IOException) {}
            //scrivo il risultato sul responseTextView
            override fun onResponse(call: Call, response: Response) = writeToResponseTextView(response.body()!!.string())
        })
    }

    fun writeToResponseTextView(s: String){
        //uso runOnUiThread perché se modifico qualcosa dell'UI da un thread diverso da quello che l'ha creata mi da errore, quindi devo modificarlo
        //dal suo thread
        //In particolare la modifica che faccio qui è assegnare al responseTextView la stringa che mi viene passata, in modo che possa essere visualizzata
        this@MainActivity.runOnUiThread(java.lang.Runnable {
            responseTextView.text = s
        })
    }

}