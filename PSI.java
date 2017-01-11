import java.util.Iterator;
import java.util.*;



import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.WritableComparable;
import org.apache.hadoop.io.WritableComparator;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.FileSplit;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;




public class PSI extends Configured implements Tool{

	public static void main(String[] args) throws Exception {
		Tool tool = new PSI(); 
		ToolRunner.run(tool, args);
		
	}

	@Override
	public int run(String[] args) throws Exception {
		Configuration conf = getConf();
		Job job = new Job(conf);
		job.setJarByClass(getClass());
		
		FileSystem fs = FileSystem.get(conf);
		fs.delete(new Path(args[1]), true);
		

		FileInputFormat.addInputPath(job, new Path(args[0]));
		FileOutputFormat.setOutputPath(job, new Path(args[1]));
		
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(IntWritable.class);
		
		job.setMapperClass(PSIMap.class);
		job.setReducerClass(PSIReduce.class);
		
		job.waitForCompletion(true);
		return 0;
	}

	
	
	
	
}

class PSIMap extends Mapper<LongWritable, Text, Text, IntWritable>{
	
	protected void map(LongWritable key, Text value,Context context) throws java.io.IOException ,InterruptedException {
		String[] PSIrate = value.toString().split(",");
		String keyy;
		float rate = Float.parseFloat(PSIrate[1]);
		if (rate < 100) keyy = "rate<100";
		else if (rate >= 100 && rate < 150) keyy = "rate100~150";	
		else if (rate >= 150 && rate < 200) keyy = "rate150~200";
		else keyy = "rate>200";	
		IntWritable one = new IntWritable(1);
		context.write(new Text(keyy),one);	
	};
}


class PSIReduce extends Reducer<Text, IntWritable,Text, IntWritable>{
	private IntWritable result = new IntWritable();
	protected void reduce(Text key,Iterable<IntWritable> values, Context context) throws java.io.IOException ,InterruptedException {
		int sum = 0;
		for (IntWritable val : values) {
			sum += val.get();
		}
		result.set(sum);
		context.write(key, result);
	};
	
}



