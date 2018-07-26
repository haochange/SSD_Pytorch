# -*- coding: utf-8 -*-
# Written by yq_yao

import torch
import torch.nn as nn
from data import channels_config
import os

def dense_conv1(channels):
    layers = []
    layers.append(nn.MaxPool2d(kernel_size=2, stride=2, ceil_mode=True))
    layers.append(nn.MaxPool2d(kernel_size=2, stride=2, ceil_mode=True))
    layers.append(nn.MaxPool2d(kernel_size=2, stride=2, ceil_mode=True))
    layers.append(nn.Conv2d(256, channels[0], kernel_size=3, padding=1))
    layers.append(nn.Conv2d(256, channels[1], kernel_size=3, padding=1))
    layers.append(nn.Conv2d(256, channels[2], kernel_size=3, padding=1))
    return layers

def dense_conv2(channels):
    layers = []
    layers.append(nn.MaxPool2d(kernel_size=2, stride=2, ceil_mode=True))
    layers.append(nn.MaxPool2d(kernel_size=2, stride=2, ceil_mode=True))
    layers.append(nn.MaxPool2d(kernel_size=2, stride=2, ceil_mode=True))
    layers.append(nn.Conv2d(512, channels[0], kernel_size=3, padding=1))
    layers.append(nn.Conv2d(512, channels[1], kernel_size=3, padding=1))
    layers.append(nn.Conv2d(512, channels[2], kernel_size=3, padding=1))    
    return layers

def dense_conv3(channels):
    layers = []
    layers.append(nn.Conv2d(1024, channels[0], kernel_size=3, padding=1))
    layers.append(nn.Upsample(scale_factor=2, mode='bilinear'))
    layers.append(nn.MaxPool2d(kernel_size=2, stride=2, ceil_mode=True))
    layers.append(nn.MaxPool2d(kernel_size=2, stride=2, ceil_mode=True))
    layers.append(nn.Conv2d(1024, channels[1], kernel_size=3, padding=1))
    layers.append(nn.Conv2d(1024, channels[2], kernel_size=3, padding=1))
    return layers

def dense_conv4_res_300(channels):
    layers = []
    layers.append(nn.Conv2d(2048, channels[0], kernel_size=3, padding=1))
    layers.append(nn.Conv2d(2048, channels[1], kernel_size=3, padding=1))
    layers.append(nn.Upsample(size=(19, 19), mode='bilinear'))
    layers.append(nn.Upsample(size=(38, 38), mode='bilinear'))
    layers.append(nn.MaxPool2d(kernel_size=2, stride=2, ceil_mode=True))
    layers.append(nn.Conv2d(2048, channels[2], kernel_size=3, padding=1))
    return layers

def dense_conv4_vgg_300(channels):
    layers  = []
    layers.append(nn.Conv2d(512, channels[0], kernel_size=3, padding=1))
    layers.append(nn.Conv2d(512, channels[1], kernel_size=3, padding=1))
    layers.append(nn.Upsample(size=(19, 19), mode='bilinear'))
    layers.append(nn.Upsample(size=(38, 38), mode='bilinear'))
    layers.append(nn.MaxPool2d(kernel_size=2, stride=2, ceil_mode=True))
    layers.append(nn.Conv2d(512, channels[2], kernel_size=3, padding=1))    
    return layers

def dense_conv4_vgg_512(channels):
    layers  = []
    layers.append(nn.Conv2d(512, channels[0], kernel_size=3, padding=1))
    layers.append(nn.Conv2d(512, channels[1], kernel_size=3, padding=1))
    layers.append(nn.Upsample(scale_factor=2, mode='bilinear'))
    layers.append(nn.Upsample(scale_factor=4, mode='bilinear'))
    layers.append(nn.MaxPool2d(kernel_size=2, stride=2, ceil_mode=True))
    layers.append(nn.Conv2d(512, channels[2], kernel_size=3, padding=1))    
    return layers   


def dense_conv4_res_512(channels):
    layers = []
    layers.append(nn.Conv2d(2048, channels[0], kernel_size=3, padding=1))
    layers.append(nn.Conv2d(2048, channels[1], kernel_size=3, padding=1))
    layers.append(nn.Upsample(scale_factor=2, mode='bilinear'))
    layers.append(nn.Upsample(scale_factor=4, mode='bilinear'))
    layers.append(nn.MaxPool2d(kernel_size=2, stride=2, ceil_mode=True))
    layers.append(nn.Conv2d(2048, channels[2], kernel_size=3, padding=1))
    return layers

def dense_conv5_vgg_300(channels):
    layers = []
    layers.append(nn.Conv2d(256, channels[0], kernel_size=3, padding=1))
    layers.append(nn.Conv2d(256, channels[1], kernel_size=3, padding=1))
    layers.append(nn.Conv2d(256, channels[2], kernel_size=3, padding=1))
    layers.append(nn.Upsample(size=(10, 10), mode='bilinear'))
    layers.append(nn.Upsample(size=(19, 19), mode='bilinear'))
    layers.append(nn.Upsample(size=(38, 38), mode='bilinear'))
    return layers

def dense_conv5_vgg_512(channels):
    #5x5
    layers = []
    layers.append(nn.Conv2d(256, channels[0], kernel_size=3, padding=1))
    layers.append(nn.Conv2d(256, channels[1], kernel_size=3, padding=1))
    layers.append(nn.Conv2d(256, channels[2], kernel_size=3, padding=1))
    layers.append(nn.Upsample(scale_factor=2, mode='bilinear'))
    layers.append(nn.Upsample(scale_factor=4, mode='bilinear'))
    layers.append(nn.Upsample(scale_factor=8, mode='bilinear'))
    return layers

def dense_conv5_res_300(channels):
    layers = []
    layers.append(nn.Conv2d(256, channels[0], kernel_size=3, padding=1))
    layers.append(nn.Conv2d(256, channels[1], kernel_size=3, padding=1))
    layers.append(nn.Conv2d(256, channels[2], kernel_size=3, padding=1))
    layers.append(nn.Upsample(size=(10, 10), mode='bilinear'))
    layers.append(nn.Upsample(size=(19, 19), mode='bilinear'))
    layers.append(nn.Upsample(size=(38, 38), mode='bilinear'))
    return layers

def dense_conv5_res_512(channels):
    #5x5
    layers = []
    layers.append(nn.Conv2d(256, channels[0], kernel_size=3, padding=1))
    layers.append(nn.Conv2d(256, channels[1], kernel_size=3, padding=1))
    layers.append(nn.Conv2d(256, channels[2], kernel_size=3, padding=1))
    layers.append(nn.Upsample(scale_factor=2, mode='bilinear'))
    layers.append(nn.Upsample(scale_factor=4, mode='bilinear'))
    layers.append(nn.Upsample(scale_factor=8, mode='bilinear'))
    return layers

def dense_concat(channels):
    layers = []
    layers.append(nn.Conv2d(channels[0], 512, kernel_size=1, padding=0))
    layers.append(nn.Conv2d(channels[1], 1024, kernel_size=1, padding=0))
    layers.append(nn.Conv2d(channels[2], 512, kernel_size=1, padding=0))
    layers.append(nn.Conv2d(channels[3], 256, kernel_size=1, padding=0))
    return layers

def dense_list_vgg(channel, size):
    cfg = channels_config[channel]
    dense_list_ = []
    if size == 300:
        dense_list_ = [dense_conv1(cfg[0]), dense_conv2(cfg[1]), dense_conv3(cfg[2]), dense_conv4_vgg_300(cfg[3]), dense_conv5_vgg_300(cfg[4]), dense_concat(cfg[5])]
    else:
        dense_list_ = [dense_conv1(cfg[0]), dense_conv2(cfg[1]), dense_conv3(cfg[2]), dense_conv4_vgg_512(cfg[3]), dense_conv5_vgg_512(cfg[4]), dense_concat(cfg[5])]
    return dense_list_


def dense_list_res(channel, size):
    cfg = channels_config[channel]
    dense_list_ = []
    if size == 300:
        dense_list_ = [dense_conv1(cfg[0]), dense_conv2(cfg[1]), dense_conv3(
            cfg[2]), dense_conv4_res_300(cfg[3]), dense_conv5_res_300(cfg[4]), dense_concat(cfg[5])]
    else:
        dense_list_ = [dense_conv1(cfg[0]), dense_conv2(cfg[1]), dense_conv3(
            cfg[2]), dense_conv4_res_512(cfg[3]), dense_conv5_res_512(cfg[4]), dense_concat(cfg[5])]
    return dense_list_
