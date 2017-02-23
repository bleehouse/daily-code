package com.bleehouse;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.format.FormatterRegistry;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurerAdapter;
import com.bleehouse.converter.LocalDateTimeConverter;

import com.bleehouse.filter.HelloFilter;
import com.bleehouse.interceptor.HttpInterceptor;

@SpringBootApplication
@ComponentScan
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
            
            // https://github.com/pkainulainen/spring-from-the-trenches/blob/master/type-converters/src/test/java/net/petrikainulainen/spring/trenches/DateTimeControllerTest.java
            
            @Override
            public void addFormatters(FormatterRegistry registry) {
//                registry.addConverter(new LocalDateConverter("yyyy-MM-dd"));
                registry.addConverter(new LocalDateTimeConverter("yyyy-MM-dd'T'HH:mm:ss.SSS"));
            }            
        };
    }

}
