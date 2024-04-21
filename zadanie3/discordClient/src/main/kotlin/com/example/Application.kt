package com.example

import io.ktor.client.*
import io.ktor.client.request.*
import io.ktor.client.statement.*
import io.ktor.util.*

@OptIn(InternalAPI::class)
suspend fun main() {
    val client = HttpClient()

    try {
        val response: HttpResponse = client.post("Discord Token") {
            headers {
                append("Content-Type", "application/json")
            }
            body = "{\"content\": \"Hello World!\"}"
        }

        println(response.bodyAsText())
    } catch (e: Exception) {
        println("Error: ${e.message}")
    } finally {
        client.close()
    }
}

