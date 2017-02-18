package com.bleehouse;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurerAdapter;

import com.bleehouse.filter.HelloFilter;
import com.bleehouse.interceptor.HttpInterceptor;

@SpringBootApplication
public class SpringBootWebExampleApplication {

	public static void main(String[] args) {
		SpringApplication.run(SpringBootWebExampleApplication.class, args);
	}

	@Bean
	public HelloFilter helloFilter() {
		return new HelloFilter();
	}
	
    @Bean
    public WebMvcConfigurerAdapter webMvcConfigurerAdapter() {
        return new WebMvcConfigurerAdapter() {
            @Override
            public void addInterceptors(InterceptorRegistry registry) {
                registry.addInterceptor(new HttpInterceptor());
            }
        };
    }

}
