package com.softwareengineering.personalhw;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.IOException;

public class MySoftMapper extends Mapper<LongWritable, Text, Text, LongWritable> {
    private LongWritable outV = new LongWritable(1);

    @Override
    protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, LongWritable>.Context context) throws IOException, InterruptedException {
        context.write(value, outV);
    }
}
