require File.dirname(__FILE__) + "/../spec_helper.rb"

describe Spira::Types::String do

  context "when serializing" do
    it "should serialize strings to XSD strings" do
      serialized = Spira::Types::String.serialize("a string")
      serialized.should be_a RDF::Literal
      serialized.should == RDF::Literal.new("a string")
    end

    it "should serialize strings with language tags to XSD strings" do
      serialized = Spira::Types::String.serialize('"a string"@en')
      serialized.should be_a RDF::Literal
      serialized.should == RDF::Literal.new("a string", :language => :en)
    end

    it "should serialize other types to XSD strings" do
      serialized = Spira::Types::String.serialize(5)
      serialized.should be_a RDF::Literal
      serialized.should == RDF::Literal.new("5")
    end
  end

  context "when unserializing" do
    it "should unserialize XSD strings to strings" do
      value = Spira::Types::String.unserialize(RDF::Literal.new("a string", :datatype => RDF::XSD.string))
      value.should be_a String
      value.should == "a string"
    end

    it "should unserialize XSD strings to strings with language tags" do
      value = Spira::Types::String.unserialize(RDF::Literal.new("a string", :datatype => RDF::XSD.string, :language => :en))
      value.should be_a String
      value.should == '"a string"@en'
    end

    it "should unserialize anything else to a string" do
      value = Spira::Types::String.unserialize(RDF::Literal.new(5, :datatype => RDF::XSD.integer))
      value.should be_a String
      value.should == "5"
    end
  end


end

