val ktor_version: String by project
val kotlin_version: String by project
val logback_version: String by project

plugins {
    kotlin("jvm") version "1.9.23"
    id("io.ktor.plugin") version "2.3.10"
}

group = "com.example"
version = "0.0.1"

application {
    mainClass.set("com.example.ApplicationKt")

    val isDevelopment: Boolean = project.ext.has("development")
    applicationDefaultJvmArgs = listOf("-Dio.ktor.development=$isDevelopment")
}

repositories {
    mavenCentral()
}

dependencies {
    implementation("io.ktor:ktor-client-core:{version}")
    implementation("io.ktor:ktor-client-json:{version}") // if you need JSON support
    implementation("io.ktor:ktor-client-logging:{version}") // if you need logging
    implementation("io.ktor:ktor-client-cio:{version}") // or use ktor-client-okhttp for OkHttp client
}
