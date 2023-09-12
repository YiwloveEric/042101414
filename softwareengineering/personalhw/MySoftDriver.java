package com.softwareengineering.personalhw;


import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

import java.io.IOException;

public class MySoftDriver {
    public static void main(String[] args) throws IOException, InterruptedException, ClassNotFoundException {
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf);
        job.setJarByClass(MySoftDriver.class);
        job.setMapperClass(MySoftMapper.class);
        job.setReducerClass(MySoftReducer.class);
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(LongWritable.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(LongWritable.class);
        FileInputFormat.setInputPaths(job, new Path("D:\\input\\softwareengineering"));
        FileOutputFormat.setOutputPath(job, new Path("D:\\hadoop\\softwareoutput8"));
        boolean result = job.waitForCompletion(true);
        System.exit(result ? 0 : 1);
    }
}
